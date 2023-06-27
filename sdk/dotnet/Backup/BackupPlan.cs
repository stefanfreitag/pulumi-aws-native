// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Backup
{
    /// <summary>
    /// Resource Type definition for AWS::Backup::BackupPlan
    /// </summary>
    [AwsNativeResourceType("aws-native:backup:BackupPlan")]
    public partial class BackupPlan : global::Pulumi.CustomResource
    {
        [Output("backupPlan")]
        public Output<Outputs.BackupPlanResourceType> BackupPlanValue { get; private set; } = null!;

        [Output("backupPlanArn")]
        public Output<string> BackupPlanArn { get; private set; } = null!;

        [Output("backupPlanId")]
        public Output<string> BackupPlanId { get; private set; } = null!;

        [Output("backupPlanTags")]
        public Output<object?> BackupPlanTags { get; private set; } = null!;

        [Output("versionId")]
        public Output<string> VersionId { get; private set; } = null!;


        /// <summary>
        /// Create a BackupPlan resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public BackupPlan(string name, BackupPlanArgs args, CustomResourceOptions? options = null)
            : base("aws-native:backup:BackupPlan", name, args ?? new BackupPlanArgs(), MakeResourceOptions(options, ""))
        {
        }

        private BackupPlan(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:backup:BackupPlan", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing BackupPlan resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static BackupPlan Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new BackupPlan(name, id, options);
        }
    }

    public sealed class BackupPlanArgs : global::Pulumi.ResourceArgs
    {
        [Input("backupPlan", required: true)]
        public Input<Inputs.BackupPlanResourceTypeArgs> BackupPlanValue { get; set; } = null!;

        [Input("backupPlanTags")]
        public Input<object>? BackupPlanTags { get; set; }

        public BackupPlanArgs()
        {
        }
        public static new BackupPlanArgs Empty => new BackupPlanArgs();
    }
}
