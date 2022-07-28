// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Inputs
{

    /// <summary>
    /// Ground truth input provided in S3 
    /// </summary>
    public sealed class ModelBiasJobDefinitionMonitoringGroundTruthS3InputArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A URI that identifies the Amazon S3 storage location where Amazon SageMaker saves the results of a monitoring job.
        /// </summary>
        [Input("s3Uri", required: true)]
        public Input<string> S3Uri { get; set; } = null!;

        public ModelBiasJobDefinitionMonitoringGroundTruthS3InputArgs()
        {
        }
        public static new ModelBiasJobDefinitionMonitoringGroundTruthS3InputArgs Empty => new ModelBiasJobDefinitionMonitoringGroundTruthS3InputArgs();
    }
}
