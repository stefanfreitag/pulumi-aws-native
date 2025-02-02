// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardParameterDeclarationArgs : global::Pulumi.ResourceArgs
    {
        [Input("dateTimeParameterDeclaration")]
        public Input<Inputs.DashboardDateTimeParameterDeclarationArgs>? DateTimeParameterDeclaration { get; set; }

        [Input("decimalParameterDeclaration")]
        public Input<Inputs.DashboardDecimalParameterDeclarationArgs>? DecimalParameterDeclaration { get; set; }

        [Input("integerParameterDeclaration")]
        public Input<Inputs.DashboardIntegerParameterDeclarationArgs>? IntegerParameterDeclaration { get; set; }

        [Input("stringParameterDeclaration")]
        public Input<Inputs.DashboardStringParameterDeclarationArgs>? StringParameterDeclaration { get; set; }

        public DashboardParameterDeclarationArgs()
        {
        }
        public static new DashboardParameterDeclarationArgs Empty => new DashboardParameterDeclarationArgs();
    }
}
