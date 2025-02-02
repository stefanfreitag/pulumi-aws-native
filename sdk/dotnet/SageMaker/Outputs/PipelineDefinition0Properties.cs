// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Outputs
{

    [OutputType]
    public sealed class PipelineDefinition0Properties
    {
        /// <summary>
        /// A specification that defines the pipeline in JSON format.
        /// </summary>
        public readonly string PipelineDefinitionBody;

        [OutputConstructor]
        private PipelineDefinition0Properties(string pipelineDefinitionBody)
        {
            PipelineDefinitionBody = pipelineDefinitionBody;
        }
    }
}
