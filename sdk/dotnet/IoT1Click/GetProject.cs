// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT1Click
{
    public static class GetProject
    {
        /// <summary>
        /// Resource Type definition for AWS::IoT1Click::Project
        /// </summary>
        public static Task<GetProjectResult> InvokeAsync(GetProjectArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetProjectResult>("aws-native:iot1click:getProject", args ?? new GetProjectArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::IoT1Click::Project
        /// </summary>
        public static Output<GetProjectResult> Invoke(GetProjectInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetProjectResult>("aws-native:iot1click:getProject", args ?? new GetProjectInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetProjectArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetProjectArgs()
        {
        }
        public static new GetProjectArgs Empty => new GetProjectArgs();
    }

    public sealed class GetProjectInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetProjectInvokeArgs()
        {
        }
        public static new GetProjectInvokeArgs Empty => new GetProjectInvokeArgs();
    }


    [OutputType]
    public sealed class GetProjectResult
    {
        public readonly string? Arn;
        public readonly string? Description;
        public readonly string? Id;
        public readonly Outputs.ProjectPlacementTemplate? PlacementTemplate;

        [OutputConstructor]
        private GetProjectResult(
            string? arn,

            string? description,

            string? id,

            Outputs.ProjectPlacementTemplate? placementTemplate)
        {
            Arn = arn;
            Description = description;
            Id = id;
            PlacementTemplate = placementTemplate;
        }
    }
}
