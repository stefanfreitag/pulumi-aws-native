// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodeDeploy.Inputs
{

    public sealed class DeploymentGroupTargetGroupInfoArgs : global::Pulumi.ResourceArgs
    {
        [Input("name")]
        public Input<string>? Name { get; set; }

        public DeploymentGroupTargetGroupInfoArgs()
        {
        }
        public static new DeploymentGroupTargetGroupInfoArgs Empty => new DeploymentGroupTargetGroupInfoArgs();
    }
}
