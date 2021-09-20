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
    /// The output configuration for monitoring jobs.
    /// </summary>
    public sealed class ModelExplainabilityJobDefinitionMonitoringOutputConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        [Input("monitoringOutputs", required: true)]
        private InputList<Inputs.ModelExplainabilityJobDefinitionMonitoringOutputArgs>? _monitoringOutputs;

        /// <summary>
        /// Monitoring outputs for monitoring jobs. This is where the output of the periodic monitoring jobs is uploaded.
        /// </summary>
        public InputList<Inputs.ModelExplainabilityJobDefinitionMonitoringOutputArgs> MonitoringOutputs
        {
            get => _monitoringOutputs ?? (_monitoringOutputs = new InputList<Inputs.ModelExplainabilityJobDefinitionMonitoringOutputArgs>());
            set => _monitoringOutputs = value;
        }

        public ModelExplainabilityJobDefinitionMonitoringOutputConfigArgs()
        {
        }
    }
}
