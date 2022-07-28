// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ECS.Inputs
{

    public sealed class TaskDefinitionPortMappingArgs : global::Pulumi.ResourceArgs
    {
        [Input("containerPort")]
        public Input<int>? ContainerPort { get; set; }

        [Input("hostPort")]
        public Input<int>? HostPort { get; set; }

        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        public TaskDefinitionPortMappingArgs()
        {
        }
        public static new TaskDefinitionPortMappingArgs Empty => new TaskDefinitionPortMappingArgs();
    }
}
