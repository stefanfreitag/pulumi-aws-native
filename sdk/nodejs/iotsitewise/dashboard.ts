// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::IoTSiteWise::Dashboard
 */
export class Dashboard extends pulumi.CustomResource {
    /**
     * Get an existing Dashboard resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Dashboard {
        return new Dashboard(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iotsitewise:Dashboard';

    /**
     * Returns true if the given object is an instance of Dashboard.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Dashboard {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Dashboard.__pulumiType;
    }

    /**
     * The ARN of the dashboard.
     */
    public /*out*/ readonly dashboardArn!: pulumi.Output<string>;
    /**
     * The dashboard definition specified in a JSON literal.
     */
    public readonly dashboardDefinition!: pulumi.Output<string>;
    /**
     * A description for the dashboard.
     */
    public readonly dashboardDescription!: pulumi.Output<string>;
    /**
     * The ID of the dashboard.
     */
    public /*out*/ readonly dashboardId!: pulumi.Output<string>;
    /**
     * A friendly name for the dashboard.
     */
    public readonly dashboardName!: pulumi.Output<string>;
    /**
     * The ID of the project in which to create the dashboard.
     */
    public readonly projectId!: pulumi.Output<string | undefined>;
    /**
     * A list of key-value pairs that contain metadata for the dashboard.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a Dashboard resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DashboardArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.dashboardDefinition === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dashboardDefinition'");
            }
            if ((!args || args.dashboardDescription === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dashboardDescription'");
            }
            resourceInputs["dashboardDefinition"] = args ? args.dashboardDefinition : undefined;
            resourceInputs["dashboardDescription"] = args ? args.dashboardDescription : undefined;
            resourceInputs["dashboardName"] = args ? args.dashboardName : undefined;
            resourceInputs["projectId"] = args ? args.projectId : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["dashboardArn"] = undefined /*out*/;
            resourceInputs["dashboardId"] = undefined /*out*/;
        } else {
            resourceInputs["dashboardArn"] = undefined /*out*/;
            resourceInputs["dashboardDefinition"] = undefined /*out*/;
            resourceInputs["dashboardDescription"] = undefined /*out*/;
            resourceInputs["dashboardId"] = undefined /*out*/;
            resourceInputs["dashboardName"] = undefined /*out*/;
            resourceInputs["projectId"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["projectId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Dashboard.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Dashboard resource.
 */
export interface DashboardArgs {
    /**
     * The dashboard definition specified in a JSON literal.
     */
    dashboardDefinition: pulumi.Input<string>;
    /**
     * A description for the dashboard.
     */
    dashboardDescription: pulumi.Input<string>;
    /**
     * A friendly name for the dashboard.
     */
    dashboardName?: pulumi.Input<string>;
    /**
     * The ID of the project in which to create the dashboard.
     */
    projectId?: pulumi.Input<string>;
    /**
     * A list of key-value pairs that contain metadata for the dashboard.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
