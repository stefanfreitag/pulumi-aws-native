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
    /// The Json format
    /// </summary>
    public sealed class ModelBiasJobDefinitionJsonArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A boolean flag indicating if it is JSON line format
        /// </summary>
        [Input("line")]
        public Input<bool>? Line { get; set; }

        public ModelBiasJobDefinitionJsonArgs()
        {
        }
        public static new ModelBiasJobDefinitionJsonArgs Empty => new ModelBiasJobDefinitionJsonArgs();
    }
}
