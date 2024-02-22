// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Amplify
{
    /// <summary>
    /// The AWS::Amplify::Branch resource creates a new branch within an app.
    /// </summary>
    [AwsNativeResourceType("aws-native:amplify:Branch")]
    public partial class Branch : global::Pulumi.CustomResource
    {
        [Output("appId")]
        public Output<string> AppId { get; private set; } = null!;

        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("backend")]
        public Output<Outputs.BranchBackend?> Backend { get; private set; } = null!;

        [Output("basicAuthConfig")]
        public Output<Outputs.BranchBasicAuthConfig?> BasicAuthConfig { get; private set; } = null!;

        [Output("branchName")]
        public Output<string> BranchName { get; private set; } = null!;

        [Output("buildSpec")]
        public Output<string?> BuildSpec { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("enableAutoBuild")]
        public Output<bool?> EnableAutoBuild { get; private set; } = null!;

        [Output("enablePerformanceMode")]
        public Output<bool?> EnablePerformanceMode { get; private set; } = null!;

        [Output("enablePullRequestPreview")]
        public Output<bool?> EnablePullRequestPreview { get; private set; } = null!;

        [Output("environmentVariables")]
        public Output<ImmutableArray<Outputs.BranchEnvironmentVariable>> EnvironmentVariables { get; private set; } = null!;

        [Output("framework")]
        public Output<string?> Framework { get; private set; } = null!;

        [Output("pullRequestEnvironmentName")]
        public Output<string?> PullRequestEnvironmentName { get; private set; } = null!;

        [Output("stage")]
        public Output<Pulumi.AwsNative.Amplify.BranchStage?> Stage { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Branch resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Branch(string name, BranchArgs args, CustomResourceOptions? options = null)
            : base("aws-native:amplify:Branch", name, args ?? new BranchArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Branch(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:amplify:Branch", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "appId",
                    "branchName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Branch resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Branch Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Branch(name, id, options);
        }
    }

    public sealed class BranchArgs : global::Pulumi.ResourceArgs
    {
        [Input("appId", required: true)]
        public Input<string> AppId { get; set; } = null!;

        [Input("backend")]
        public Input<Inputs.BranchBackendArgs>? Backend { get; set; }

        [Input("basicAuthConfig")]
        public Input<Inputs.BranchBasicAuthConfigArgs>? BasicAuthConfig { get; set; }

        [Input("branchName")]
        public Input<string>? BranchName { get; set; }

        [Input("buildSpec")]
        public Input<string>? BuildSpec { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("enableAutoBuild")]
        public Input<bool>? EnableAutoBuild { get; set; }

        [Input("enablePerformanceMode")]
        public Input<bool>? EnablePerformanceMode { get; set; }

        [Input("enablePullRequestPreview")]
        public Input<bool>? EnablePullRequestPreview { get; set; }

        [Input("environmentVariables")]
        private InputList<Inputs.BranchEnvironmentVariableArgs>? _environmentVariables;
        public InputList<Inputs.BranchEnvironmentVariableArgs> EnvironmentVariables
        {
            get => _environmentVariables ?? (_environmentVariables = new InputList<Inputs.BranchEnvironmentVariableArgs>());
            set => _environmentVariables = value;
        }

        [Input("framework")]
        public Input<string>? Framework { get; set; }

        [Input("pullRequestEnvironmentName")]
        public Input<string>? PullRequestEnvironmentName { get; set; }

        [Input("stage")]
        public Input<Pulumi.AwsNative.Amplify.BranchStage>? Stage { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public BranchArgs()
        {
        }
        public static new BranchArgs Empty => new BranchArgs();
    }
}
