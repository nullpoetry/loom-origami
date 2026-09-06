openapi: 3.0.0
info:
  title: Loom Data Ingestion API
  version: 1.0.0
  description: API for ingesting raw and pre-processed telemetry into the Pure Byte Data Loom.
  contact:
    name: Loom Origami Maintainers
    email: ops@example.com

servers:
  - url: http://localhost:8080/loom-api
    description: Local development server

paths:
  /data/network-flow:
    post:
      summary: Ingest raw network flow data (from XDP/eBPF)
      operationId: ingestNetworkFlow
      tags:
        - ingestion
      requestBody:
        description: Raw packet bytes; the request body should be sent with Content-Type: application/octet-stream
        required: true
        content:
          application/octet-stream:
            schema:
              type: string
              format: binary
            examples:
              rawPacket:
                summary: Example raw packet bytes (placeholder)
                value: "raw_packet_bytes..." 
      responses:
        '202':
          description: Data accepted for processing.
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                  size:
                    type: integer
                required:
                  - status
              examples:
                accepted:
                  value:
                    status: accepted
                    size: 1234

  /data/system-metrics:
    post:
      summary: Ingest structured system metrics
      operationId: ingestSystemMetrics
      tags:
        - ingestion
      requestBody:
        description: Structured system metric event
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SystemMetrics'
            examples:
              cpuMetric:
                summary: Example CPU metric
                value:
                  timestamp: "2026-09-06T12:34:56Z"
                  source_id: "host-01"
                  metric_name: "cpu.utilization"
                  value: 12.34
      responses:
        '202':
          description: Metrics accepted.
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                  metric:
                    type: string
                required:
                  - status
              examples:
                accepted:
                  value:
                    status: accepted
                    metric: cpu.utilization

components:
  schemas:
    SystemMetrics:
      type: object
      required:
        - timestamp
        - source_id
        - metric_name
        - value
      properties:
        timestamp:
          type: string
          format: date-time
          description: ISO 8601 timestamp for the metric
        source_id:
          type: string
          description: Unique ID of the host/source emitting the metric
        metric_name:
          type: string
          description: Name of the metric
        value:
          type: number
          description: Numeric value of the metric
      additionalProperties: false
