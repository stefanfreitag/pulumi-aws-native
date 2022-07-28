// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3ObjectLambda.Inputs
{

    /// <summary>
    /// Configuration to define what content transformation will be applied on which S3 Action.
    /// </summary>
    public sealed class AccessPointTransformationConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("actions", required: true)]
        private InputList<string>? _actions;
        public InputList<string> Actions
        {
            get => _actions ?? (_actions = new InputList<string>());
            set => _actions = value;
        }

        [Input("contentTransformation", required: true)]
        public Input<object> ContentTransformation { get; set; } = null!;

        public AccessPointTransformationConfigurationArgs()
        {
        }
        public static new AccessPointTransformationConfigurationArgs Empty => new AccessPointTransformationConfigurationArgs();
    }
}
