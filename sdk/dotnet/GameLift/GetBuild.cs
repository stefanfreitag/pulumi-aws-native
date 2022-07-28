// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GameLift
{
    public static class GetBuild
    {
        /// <summary>
        /// Resource Type definition for AWS::GameLift::Build
        /// </summary>
        public static Task<GetBuildResult> InvokeAsync(GetBuildArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetBuildResult>("aws-native:gamelift:getBuild", args ?? new GetBuildArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::GameLift::Build
        /// </summary>
        public static Output<GetBuildResult> Invoke(GetBuildInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetBuildResult>("aws-native:gamelift:getBuild", args ?? new GetBuildInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetBuildArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetBuildArgs()
        {
        }
        public static new GetBuildArgs Empty => new GetBuildArgs();
    }

    public sealed class GetBuildInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetBuildInvokeArgs()
        {
        }
        public static new GetBuildInvokeArgs Empty => new GetBuildInvokeArgs();
    }


    [OutputType]
    public sealed class GetBuildResult
    {
        public readonly string? Id;
        public readonly string? Name;
        public readonly string? Version;

        [OutputConstructor]
        private GetBuildResult(
            string? id,

            string? name,

            string? version)
        {
            Id = id;
            Name = name;
            Version = version;
        }
    }
}
