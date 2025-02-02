// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Inputs
{

    public sealed class ModelImageConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("repositoryAccessMode", required: true)]
        public Input<string> RepositoryAccessMode { get; set; } = null!;

        [Input("repositoryAuthConfig")]
        public Input<Inputs.ModelRepositoryAuthConfigArgs>? RepositoryAuthConfig { get; set; }

        public ModelImageConfigArgs()
        {
        }
        public static new ModelImageConfigArgs Empty => new ModelImageConfigArgs();
    }
}
