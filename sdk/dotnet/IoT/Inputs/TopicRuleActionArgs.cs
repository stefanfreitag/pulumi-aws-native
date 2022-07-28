// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT.Inputs
{

    public sealed class TopicRuleActionArgs : global::Pulumi.ResourceArgs
    {
        [Input("cloudwatchAlarm")]
        public Input<Inputs.TopicRuleCloudwatchAlarmActionArgs>? CloudwatchAlarm { get; set; }

        [Input("cloudwatchLogs")]
        public Input<Inputs.TopicRuleCloudwatchLogsActionArgs>? CloudwatchLogs { get; set; }

        [Input("cloudwatchMetric")]
        public Input<Inputs.TopicRuleCloudwatchMetricActionArgs>? CloudwatchMetric { get; set; }

        [Input("dynamoDB")]
        public Input<Inputs.TopicRuleDynamoDBActionArgs>? DynamoDB { get; set; }

        [Input("dynamoDBv2")]
        public Input<Inputs.TopicRuleDynamoDBv2ActionArgs>? DynamoDBv2 { get; set; }

        [Input("elasticsearch")]
        public Input<Inputs.TopicRuleElasticsearchActionArgs>? Elasticsearch { get; set; }

        [Input("firehose")]
        public Input<Inputs.TopicRuleFirehoseActionArgs>? Firehose { get; set; }

        [Input("http")]
        public Input<Inputs.TopicRuleHttpActionArgs>? Http { get; set; }

        [Input("iotAnalytics")]
        public Input<Inputs.TopicRuleIotAnalyticsActionArgs>? IotAnalytics { get; set; }

        [Input("iotEvents")]
        public Input<Inputs.TopicRuleIotEventsActionArgs>? IotEvents { get; set; }

        [Input("iotSiteWise")]
        public Input<Inputs.TopicRuleIotSiteWiseActionArgs>? IotSiteWise { get; set; }

        [Input("kafka")]
        public Input<Inputs.TopicRuleKafkaActionArgs>? Kafka { get; set; }

        [Input("kinesis")]
        public Input<Inputs.TopicRuleKinesisActionArgs>? Kinesis { get; set; }

        [Input("lambda")]
        public Input<Inputs.TopicRuleLambdaActionArgs>? Lambda { get; set; }

        [Input("openSearch")]
        public Input<Inputs.TopicRuleOpenSearchActionArgs>? OpenSearch { get; set; }

        [Input("republish")]
        public Input<Inputs.TopicRuleRepublishActionArgs>? Republish { get; set; }

        [Input("s3")]
        public Input<Inputs.TopicRuleS3ActionArgs>? S3 { get; set; }

        [Input("sns")]
        public Input<Inputs.TopicRuleSnsActionArgs>? Sns { get; set; }

        [Input("sqs")]
        public Input<Inputs.TopicRuleSqsActionArgs>? Sqs { get; set; }

        [Input("stepFunctions")]
        public Input<Inputs.TopicRuleStepFunctionsActionArgs>? StepFunctions { get; set; }

        [Input("timestream")]
        public Input<Inputs.TopicRuleTimestreamActionArgs>? Timestream { get; set; }

        public TopicRuleActionArgs()
        {
        }
        public static new TopicRuleActionArgs Empty => new TopicRuleActionArgs();
    }
}
