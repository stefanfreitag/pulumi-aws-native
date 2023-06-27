// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.LakeFormation.Inputs
{

    public sealed class PermissionsResourceArgs : global::Pulumi.ResourceArgs
    {
        [Input("dataLocationResource")]
        public Input<Inputs.PermissionsDataLocationResourceArgs>? DataLocationResource { get; set; }

        [Input("databaseResource")]
        public Input<Inputs.PermissionsDatabaseResourceArgs>? DatabaseResource { get; set; }

        [Input("tableResource")]
        public Input<Inputs.PermissionsTableResourceArgs>? TableResource { get; set; }

        [Input("tableWithColumnsResource")]
        public Input<Inputs.PermissionsTableWithColumnsResourceArgs>? TableWithColumnsResource { get; set; }

        public PermissionsResourceArgs()
        {
        }
        public static new PermissionsResourceArgs Empty => new PermissionsResourceArgs();
    }
}
