// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight
{
    /// <summary>
    /// Definition of the AWS::QuickSight::Theme Resource Type.
    /// </summary>
    [AwsNativeResourceType("aws-native:quicksight:Theme")]
    public partial class Theme : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("awsAccountId")]
        public Output<string> AwsAccountId { get; private set; } = null!;

        [Output("baseThemeId")]
        public Output<string> BaseThemeId { get; private set; } = null!;

        [Output("configuration")]
        public Output<Outputs.ThemeConfiguration> Configuration { get; private set; } = null!;

        [Output("createdTime")]
        public Output<string> CreatedTime { get; private set; } = null!;

        [Output("lastUpdatedTime")]
        public Output<string> LastUpdatedTime { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("permissions")]
        public Output<ImmutableArray<Outputs.ThemeResourcePermission>> Permissions { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        [Output("themeId")]
        public Output<string> ThemeId { get; private set; } = null!;

        [Output("type")]
        public Output<Pulumi.AwsNative.QuickSight.ThemeType> Type { get; private set; } = null!;

        [Output("version")]
        public Output<Outputs.ThemeVersion> Version { get; private set; } = null!;

        [Output("versionDescription")]
        public Output<string?> VersionDescription { get; private set; } = null!;


        /// <summary>
        /// Create a Theme resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Theme(string name, ThemeArgs args, CustomResourceOptions? options = null)
            : base("aws-native:quicksight:Theme", name, args ?? new ThemeArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Theme(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:quicksight:Theme", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "awsAccountId",
                    "themeId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Theme resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Theme Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Theme(name, id, options);
        }
    }

    public sealed class ThemeArgs : global::Pulumi.ResourceArgs
    {
        [Input("awsAccountId", required: true)]
        public Input<string> AwsAccountId { get; set; } = null!;

        [Input("baseThemeId", required: true)]
        public Input<string> BaseThemeId { get; set; } = null!;

        [Input("configuration", required: true)]
        public Input<Inputs.ThemeConfigurationArgs> Configuration { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("permissions")]
        private InputList<Inputs.ThemeResourcePermissionArgs>? _permissions;
        public InputList<Inputs.ThemeResourcePermissionArgs> Permissions
        {
            get => _permissions ?? (_permissions = new InputList<Inputs.ThemeResourcePermissionArgs>());
            set => _permissions = value;
        }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        [Input("themeId", required: true)]
        public Input<string> ThemeId { get; set; } = null!;

        [Input("versionDescription")]
        public Input<string>? VersionDescription { get; set; }

        public ThemeArgs()
        {
        }
        public static new ThemeArgs Empty => new ThemeArgs();
    }
}
