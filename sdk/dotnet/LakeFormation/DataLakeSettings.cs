// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.LakeFormation
{
    /// <summary>
    /// Resource Type definition for AWS::LakeFormation::DataLakeSettings
    /// </summary>
    [Obsolete(@"DataLakeSettings is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:lakeformation:DataLakeSettings")]
    public partial class DataLakeSettings : global::Pulumi.CustomResource
    {
        [Output("admins")]
        public Output<Outputs.DataLakeSettingsAdmins?> Admins { get; private set; } = null!;

        [Output("allowExternalDataFiltering")]
        public Output<bool?> AllowExternalDataFiltering { get; private set; } = null!;

        [Output("allowFullTableExternalDataAccess")]
        public Output<bool?> AllowFullTableExternalDataAccess { get; private set; } = null!;

        [Output("authorizedSessionTagValueList")]
        public Output<ImmutableArray<string>> AuthorizedSessionTagValueList { get; private set; } = null!;

        [Output("createDatabaseDefaultPermissions")]
        public Output<Outputs.DataLakeSettingsCreateDatabaseDefaultPermissions?> CreateDatabaseDefaultPermissions { get; private set; } = null!;

        [Output("createTableDefaultPermissions")]
        public Output<Outputs.DataLakeSettingsCreateTableDefaultPermissions?> CreateTableDefaultPermissions { get; private set; } = null!;

        [Output("externalDataFilteringAllowList")]
        public Output<Outputs.DataLakeSettingsExternalDataFilteringAllowList?> ExternalDataFilteringAllowList { get; private set; } = null!;

        [Output("mutationType")]
        public Output<string?> MutationType { get; private set; } = null!;

        /// <summary>
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::LakeFormation::DataLakeSettings` for more information about the expected schema for this property.
        /// </summary>
        [Output("parameters")]
        public Output<object?> Parameters { get; private set; } = null!;

        [Output("trustedResourceOwners")]
        public Output<ImmutableArray<string>> TrustedResourceOwners { get; private set; } = null!;


        /// <summary>
        /// Create a DataLakeSettings resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DataLakeSettings(string name, DataLakeSettingsArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:lakeformation:DataLakeSettings", name, args ?? new DataLakeSettingsArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DataLakeSettings(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:lakeformation:DataLakeSettings", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing DataLakeSettings resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DataLakeSettings Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DataLakeSettings(name, id, options);
        }
    }

    public sealed class DataLakeSettingsArgs : global::Pulumi.ResourceArgs
    {
        [Input("admins")]
        public Input<Inputs.DataLakeSettingsAdminsArgs>? Admins { get; set; }

        [Input("allowExternalDataFiltering")]
        public Input<bool>? AllowExternalDataFiltering { get; set; }

        [Input("allowFullTableExternalDataAccess")]
        public Input<bool>? AllowFullTableExternalDataAccess { get; set; }

        [Input("authorizedSessionTagValueList")]
        private InputList<string>? _authorizedSessionTagValueList;
        public InputList<string> AuthorizedSessionTagValueList
        {
            get => _authorizedSessionTagValueList ?? (_authorizedSessionTagValueList = new InputList<string>());
            set => _authorizedSessionTagValueList = value;
        }

        [Input("createDatabaseDefaultPermissions")]
        public Input<Inputs.DataLakeSettingsCreateDatabaseDefaultPermissionsArgs>? CreateDatabaseDefaultPermissions { get; set; }

        [Input("createTableDefaultPermissions")]
        public Input<Inputs.DataLakeSettingsCreateTableDefaultPermissionsArgs>? CreateTableDefaultPermissions { get; set; }

        [Input("externalDataFilteringAllowList")]
        public Input<Inputs.DataLakeSettingsExternalDataFilteringAllowListArgs>? ExternalDataFilteringAllowList { get; set; }

        [Input("mutationType")]
        public Input<string>? MutationType { get; set; }

        /// <summary>
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::LakeFormation::DataLakeSettings` for more information about the expected schema for this property.
        /// </summary>
        [Input("parameters")]
        public Input<object>? Parameters { get; set; }

        [Input("trustedResourceOwners")]
        private InputList<string>? _trustedResourceOwners;
        public InputList<string> TrustedResourceOwners
        {
            get => _trustedResourceOwners ?? (_trustedResourceOwners = new InputList<string>());
            set => _trustedResourceOwners = value;
        }

        public DataLakeSettingsArgs()
        {
        }
        public static new DataLakeSettingsArgs Empty => new DataLakeSettingsArgs();
    }
}
