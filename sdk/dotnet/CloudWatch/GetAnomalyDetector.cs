// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudWatch
{
    public static class GetAnomalyDetector
    {
        /// <summary>
        /// Resource Type definition for AWS::CloudWatch::AnomalyDetector
        /// </summary>
        public static Task<GetAnomalyDetectorResult> InvokeAsync(GetAnomalyDetectorArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetAnomalyDetectorResult>("aws-native:cloudwatch:getAnomalyDetector", args ?? new GetAnomalyDetectorArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::CloudWatch::AnomalyDetector
        /// </summary>
        public static Output<GetAnomalyDetectorResult> Invoke(GetAnomalyDetectorInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetAnomalyDetectorResult>("aws-native:cloudwatch:getAnomalyDetector", args ?? new GetAnomalyDetectorInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAnomalyDetectorArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetAnomalyDetectorArgs()
        {
        }
        public static new GetAnomalyDetectorArgs Empty => new GetAnomalyDetectorArgs();
    }

    public sealed class GetAnomalyDetectorInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetAnomalyDetectorInvokeArgs()
        {
        }
        public static new GetAnomalyDetectorInvokeArgs Empty => new GetAnomalyDetectorInvokeArgs();
    }


    [OutputType]
    public sealed class GetAnomalyDetectorResult
    {
        public readonly Outputs.AnomalyDetectorConfiguration? Configuration;
        public readonly string? Id;

        [OutputConstructor]
        private GetAnomalyDetectorResult(
            Outputs.AnomalyDetectorConfiguration? configuration,

            string? id)
        {
            Configuration = configuration;
            Id = id;
        }
    }
}
