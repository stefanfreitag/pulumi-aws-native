// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.LakeFormation.Inputs
{

    public sealed class PrincipalPermissionsDataCellsFilterResourceArgs : global::Pulumi.ResourceArgs
    {
        [Input("databaseName", required: true)]
        public Input<string> DatabaseName { get; set; } = null!;

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("tableCatalogId", required: true)]
        public Input<string> TableCatalogId { get; set; } = null!;

        [Input("tableName", required: true)]
        public Input<string> TableName { get; set; } = null!;

        public PrincipalPermissionsDataCellsFilterResourceArgs()
        {
        }
        public static new PrincipalPermissionsDataCellsFilterResourceArgs Empty => new PrincipalPermissionsDataCellsFilterResourceArgs();
    }
}
