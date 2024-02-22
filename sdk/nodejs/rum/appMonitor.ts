// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::RUM::AppMonitor
 */
export class AppMonitor extends pulumi.CustomResource {
    /**
     * Get an existing AppMonitor resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): AppMonitor {
        return new AppMonitor(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:rum:AppMonitor';

    /**
     * Returns true if the given object is an instance of AppMonitor.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AppMonitor {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AppMonitor.__pulumiType;
    }

    public readonly appMonitorConfiguration!: pulumi.Output<outputs.rum.AppMonitorConfiguration | undefined>;
    public readonly customEvents!: pulumi.Output<outputs.rum.AppMonitorCustomEvents | undefined>;
    /**
     * Data collected by RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether RUM sends a copy of this telemetry data to CWLlong in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur CWLlong charges. If you omit this parameter, the default is false
     */
    public readonly cwLogEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * The top-level internet domain name for which your application has administrative authority.
     */
    public readonly domain!: pulumi.Output<string>;
    /**
     * A name for the app monitor
     */
    public readonly name!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a AppMonitor resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AppMonitorArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.domain === undefined) && !opts.urn) {
                throw new Error("Missing required property 'domain'");
            }
            resourceInputs["appMonitorConfiguration"] = args ? args.appMonitorConfiguration : undefined;
            resourceInputs["customEvents"] = args ? args.customEvents : undefined;
            resourceInputs["cwLogEnabled"] = args ? args.cwLogEnabled : undefined;
            resourceInputs["domain"] = args ? args.domain : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
        } else {
            resourceInputs["appMonitorConfiguration"] = undefined /*out*/;
            resourceInputs["customEvents"] = undefined /*out*/;
            resourceInputs["cwLogEnabled"] = undefined /*out*/;
            resourceInputs["domain"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["name"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(AppMonitor.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a AppMonitor resource.
 */
export interface AppMonitorArgs {
    appMonitorConfiguration?: pulumi.Input<inputs.rum.AppMonitorConfigurationArgs>;
    customEvents?: pulumi.Input<inputs.rum.AppMonitorCustomEventsArgs>;
    /**
     * Data collected by RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether RUM sends a copy of this telemetry data to CWLlong in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur CWLlong charges. If you omit this parameter, the default is false
     */
    cwLogEnabled?: pulumi.Input<boolean>;
    /**
     * The top-level internet domain name for which your application has administrative authority.
     */
    domain: pulumi.Input<string>;
    /**
     * A name for the app monitor
     */
    name?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
